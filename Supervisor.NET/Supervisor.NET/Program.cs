using System;
using System.Windows.Forms;

namespace Supervisor.NET
{

    class Program
    {
        [STAThread]
        static void Main()
        {
            var app = new HealthBoxClient();

            app.Menu.OptionExit.Click += (sender, args) =>
            {
                Application.Exit();
            };
            app.Menu.OptionTurnOn.Click += (sender, args) =>
            {
                app.Start();
            };
            app.Menu.OptionTurnOff.Click += (sender, args) =>
            {
                app.Stop();
            };

            app.Start();
            Application.Run();
        }
    }
}