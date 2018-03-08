using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using ShockwaveFlashObjects;
using System.Drawing.Drawing2D;
using System.IO;
using System.Threading;

namespace GithubWallpaper
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            BehindDesktopIcon.FixBehindDesktopIcon(this.Handle);
            this.FormBorderStyle = FormBorderStyle.None;
            this.Location = new Point(0, 0);
            this.Size = Screen.PrimaryScreen.Bounds.Size;
            
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            
        }


    }
}
