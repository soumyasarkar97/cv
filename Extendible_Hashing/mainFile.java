
import java.io.*;

public class mainFile 
{
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        char ch;
        int max_size, buck_size, hash_digit;
        System.out.println("Do you want to generate records?:[y/n] ");
        ch = br.readLine().charAt(0);
        System.out.println("Enter number of records: ");
        max_size = Integer.parseInt(br.readLine());
        if(ch=='y')
        {
            DatasetCreator dc = new DatasetCreator(max_size);
            dc.main(null);
        }
        
        System.out.println("Enter bucket size: ");
        buck_size = Integer.parseInt(br.readLine());
        System.out.println("Enter number of digits for hash: ");
        hash_digit = Integer.parseInt(br.readLine());
        ExtendibleHashing Obj=new ExtendibleHashing(max_size, buck_size, hash_digit);
        Bucket x = new Bucket(max_size, buck_size, hash_digit); //This is only used to recompile the bucket class everytime this method is called
        Obj.readRecords(); //All records are now stored in allRecords
        String output = Obj.extendibleHashing(); //Execute n-hashing and return the entire output to be stored in file
        OutputFileCreator op=new OutputFileCreator(output);
        op.main(null);
    }
}