using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace GIthubWallpaper
{
    class ParseGrass
    {
        private WebBrowser uri;
        private string text;
        public ParseGrass(string username)
        {
            uri.Navigate("https://github.com/" + username);
        }



    }
}
