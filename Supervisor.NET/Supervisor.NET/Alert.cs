using Newtonsoft.Json;
using Newtonsoft.Json.Serialization;

namespace Supervisor.NET
{
    [JsonObject(NamingStrategyType = typeof(CamelCaseNamingStrategy))]
    public class Alert
    {
        public string Head { get; set; }
        public string Body { get; set; }
        public string Img { get; set; }
    }
}
