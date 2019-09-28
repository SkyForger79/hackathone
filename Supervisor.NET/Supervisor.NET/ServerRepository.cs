using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;
using System.IO;
using System.Net.Http;
using System.Threading.Tasks;

namespace Supervisor.NET
{
    public class ServerRepository
    {
        public const string HOST = "http://10.70.0.243:9999/v1/";
        //public const string HOST = "http://192.168.0.101/v1/";
        public const string URL_GET_MSG = "get_msg";
        public const string URL_SEND_SNAPSHOT = "upload_file";

        public async Task<bool> SendSnapshot(Image image)
        {
            using (var client = new HttpClient())
            {
                HttpResponseMessage response = null;

                client.Timeout = new TimeSpan(0, 0, 5);
                using (var stream = new MemoryStream())
                {
                    try
                    {
                        image.Save(stream, ImageFormat.Jpeg);
                        var bytes = stream.ToArray();
                        var content = new MultipartFormDataContent();
                        content.Add(new ByteArrayContent(bytes, 0, bytes.Length), "file", "image.jpg");
                        response = await client.PostAsync(HOST + URL_SEND_SNAPSHOT, content);
                        var text = await response.Content.ReadAsStringAsync();
                        Console.WriteLine(text);
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine(ex.Message);
                    }
                }

                return response?.IsSuccessStatusCode ?? false;
            }
        }

        public async Task<List<Alert>> GetAlerts()
        {
            using (var client = new HttpClient())
            {
                client.Timeout = new TimeSpan(0, 0, 15);
                var json = await client.GetStringAsync(HOST + URL_GET_MSG);
                var alerts = JsonConvert.DeserializeObject<List<Alert>>(json);
                return alerts;
            }
        }
    }
}
