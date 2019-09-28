using System.Windows.Forms;

namespace Supervisor.NET
{
    public class Menu : ContextMenu
    {
        public readonly MenuItem OptionTurnOn = new MenuItem() { Index = 0, Text = "Включить" };
        public readonly MenuItem OptionTurnOff = new MenuItem() { Index = 1, Text = "Отключить" };
        public readonly MenuItem OptionExit = new MenuItem() { Index = 2, Text = "Выйти" };

        public Menu()
        {
            MenuItems.AddRange(new[] { OptionTurnOn, OptionTurnOff, OptionExit });
        }
    }
}