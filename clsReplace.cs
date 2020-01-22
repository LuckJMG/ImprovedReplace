using System;
using System.Collections.Generic;
using System.Text;

namespace replace
{
    public class clsReplace
    {
        //Variables
        public string String;

        //Builder
        public clsReplace(string pString)
        {
            String = pString;
        }

        //Convert string to array with spaces
        public string[] toArray(string String)
        {
                string[] newArray = String.Split(' ');
                return newArray;
        }

        //Convert commas to points
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

        //Convert points to commas
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
