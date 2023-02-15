import java.io.FileWriter;
import java.io.IOException;
import java.lang.Math;

public class DatasetCreator
{
    public static int MAX_FILE_SIZE;

    DatasetCreator(int max_size)
    {
        MAX_FILE_SIZE = max_size;
    }
    public static void random_sort(int a[])
    {
        int i=0;
        while(i<MAX_FILE_SIZE)
        {
            int random_number=(int)(Math.random()*MAX_FILE_SIZE);
            if(random_number>=MAX_FILE_SIZE)
                random_number=MAX_FILE_SIZE-1;
            //swap number at a[i] with number at a[random_number]
            int temp=a[i];
            a[i]=a[random_number];
            a[random_number]=temp;

            i++;
        } 
    }
    public static void main(String args[]) throws IOException
    {
        FileWriter dataset = new FileWriter("dataset.txt");
        String record="";
        int randomizer_transaction_id_array[] = new int[MAX_FILE_SIZE];//array to generate randomized order of transaction id
        for(int i=1; i<=MAX_FILE_SIZE; i++)
            randomizer_transaction_id_array[i-1]=i;
        
        // for(int i=1; i<=MAX_FILE_SIZE; i++)
        //     System.out.print(randomizer_transaction_id_array[i-1]+" ");
        // System.out.println();
        // System.out.println();

        random_sort(randomizer_transaction_id_array); //randomize the array

        // for(int i=1; i<=MAX_FILE_SIZE; i++)
        //     System.out.print(randomizer_transaction_id_array[i-1]+" ");
        // System.out.println();
        // System.out.println();

        for(int i=1; i<MAX_FILE_SIZE; i++)
        {
            record=randomizer_transaction_id_array[i-1]+",";
            record+= (int)(Math.random()*500000+1) + ",";
            record+= randomNameGenerator()+",";
            record+= (int)(Math.random()*1500+1)+"\n";
            dataset.write(record);
        }
        //making separate arrangement for last record so that there is no \n at the end => Tis ensures that when doing dataset_Reader.hasNextLine(), we get this as false after last record
        record=randomizer_transaction_id_array[MAX_FILE_SIZE-1]+",";
        record+= (int)(Math.random()*500000+1) + ",";
        record+= randomNameGenerator()+",";
        record+= (int)(Math.random()*1500+1); 
        dataset.write(record);

        dataset.close();
    }

    public static String randomNameGenerator()
    {
        String res="";
        res+=(char)(Math.random()*9 + 65);
        res+=(char)(Math.random()*9 + 65);
        res+=(char)(Math.random()*9 + 65);
        return res;
    }
}