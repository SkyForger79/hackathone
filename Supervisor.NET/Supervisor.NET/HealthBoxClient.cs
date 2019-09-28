using System;
using System.Windows.Forms;
using ToastNotifications;
using System.IO;
using System.Drawing;
using Emgu.CV;
using System.Drawing.Imaging;
using System.Net.Http;
using System.Threading.Tasks;
using Newtonsoft.Json;
using System.Collections.Generic;

namespace Supervisor.NET
{
    public class HealthBoxClient
    {
        public readonly NotifyIcon TrayIcon;
        public Menu Menu { get { return TrayIcon.ContextMenu as Menu; } }
        private readonly Timer captureTimer = new Timer();
        private readonly Timer checkTimer = new Timer();
        private readonly ServerRepository server = new ServerRepository();
        private int counter = 0;
        private bool locked = false;
        private int errors = 0;
        private const int MAX_ERRORS = 5;

        public HealthBoxClient()
        {
            TrayIcon = new NotifyIcon()
            {
                Icon = Properties.Resources.ApplicationIcon,
                Text = "Монитор здоровья",
                ContextMenu = new Menu(),
                Visible = true
            };
            captureTimer.Interval = 3000;
            captureTimer.Tick += async (sender, args) =>
            {
                if (!locked)
                {
                    locked = true;
                    var image = _takeFrame(counter++);
                    var success = await server.SendSnapshot(image);
                    if (success)
                    {
                        if (errors > MAX_ERRORS) Notify(Notifications.ServerBackOn);
                        errors = 0;
                    }
                    else
                    {
                        if (errors == MAX_ERRORS)
                            Notify(Notifications.ServerUnreachable);
                        errors++;
                    }
                    locked = false;
                }
            };

            checkTimer.Interval = 5000;
            checkTimer.Tick += async (sender, args) =>
            {
                try
                {
                    var alerts = await server.GetAlerts();
                    alerts.ForEach(a => Notify(Notifications.From(a)));
                }
                catch (Exception)
                {
                    Notify(Notifications.ServerUnreachable);
                }
            };
        }

        public void Start()
        {
            if (!captureTimer.Enabled) captureTimer.Start();
            //if (!checkTimer.Enabled) checkTimer.Start();
        }
        public void Stop()
        {
            if (captureTimer.Enabled) captureTimer.Stop();
            if (checkTimer.Enabled) checkTimer.Stop();
        }

        private Image _takeFrame(int counter)
        {
            VideoCapture capture = new VideoCapture(); //create a camera capture
            Bitmap image = capture.QueryFrame().Bitmap; //take a picture
            image.Save(@"c:\programming\test.jpg");
            return image;
        }

        public void Notify(Notification notification)
        {
            notification.Show();
        }
    }
}