using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace GithubWallpaper
{
    public partial class Settings : Form
    {
        public Settings()
        {
            InitializeComponent();
        }

        private void Settings_Load(object sender, EventArgs e)
        {
            notifyIcon1.ContextMenuStrip = notifyMenuStrip1;
        }
        private void 설정ToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void 일시정지ToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void 끝내기ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            notifyIcon1.Visible = false;
            Application.Exit();
        }
    }
}
