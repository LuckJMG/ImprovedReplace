using System;

namespace clsReplace
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

        //Replace commas with points
        public string CommaToPoint(string String)
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
        public string PointToComma(string String)
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
