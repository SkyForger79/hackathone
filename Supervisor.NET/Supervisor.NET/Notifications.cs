using ToastNotifications;
using System.Drawing;

namespace Supervisor.NET
{
    public static class Notifications
    {
        private static readonly FormAnimator.AnimationMethod animation = FormAnimator.AnimationMethod.Fade;
        private static readonly FormAnimator.AnimationDirection direction = FormAnimator.AnimationDirection.Up;

        private static Notification _createNotificationHelper(string header, string message, Color color, string sound = "normal")
        {
            var notification = new Notification(header, message, -1, animation, direction, color, sound);
            notification.SetIcon(Properties.Resources.icon);
            return notification;
        }

        public static Notification From(Alert alert)
        {
            return _createNotificationHelper(alert.Head, alert.Body, Color.Tomato);
        }

        public static readonly Notification Connected = _createNotificationHelper("ПОДКЛЮЧЕНИЕ УСТАНОВЛЕНО!", "Health Monitor активен.", Color.DarkGreen, "festival");

        public static readonly Notification ServerUnreachable = _createNotificationHelper("СЕРВЕР НЕДОСТУПЕН!", "Продолжаем попытки восстановить связь...", Color.Maroon, "cityscape");
        public static readonly Notification ServerBackOn = _createNotificationHelper("УСПЕХ", "Подключение восстановлено!", Color.DarkGreen, "festival");
    }
}