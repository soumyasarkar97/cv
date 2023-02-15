import java.io.FileWriter;
import java.io.IOException;
import java.lang.Math;

public class OutputFileCreator
{
    static String output_string;

    OutputFileCreator(String op)
    {
        output_string=op;
    }

    public static void main(String args[]) throws IOException
    {
        FileWriter output = new FileWriter("output.txt");
        output.write(output_string);
        output.flush();
        output.close();
    }
}