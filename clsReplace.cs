using System;
using System.Collections.Generic;
using System.Text;

namespace replace
{
    public class clsReplace
    {
        //Builder
        public clsReplace()
        {
        }

        //Convert string to array with spaces
        public string[] toArray(string String)
        {
                string[] newArray = String.Split(' ');
                return newArray;
        }

        //General Replacement
        public string SwitchChars(string String, char replacement, char replaced)
        {
            if (String.Contains(replaced))
            {
                String = String.Replace(replaced, replacement);
                return String;
            }
            else
            {
                Console.WriteLine($"The string don't have {replaced} to replace with {replacement}");
                return String;
            }
        }

        //Replace commas with points
        public string CommatoPoint(string String)
        {
            if (String.Contains(','))
            {
                String = String.Replace(',', '.');
                return String;
            }
            else
            {
                Console.WriteLine("The string don't have commas to replace");
                return String;
            }
        }

        //Replace points with commas
        public string PointtoComma(string String)
        {
            if (String.Contains('.'))
            {
                String = String.Replace('.', ',');
                return String;
            }
            else
            {
                Console.WriteLine("The string don't have points to replace");
                return String;
            }
        }

    }
}
