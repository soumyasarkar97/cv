public class Bucket 
{
    int MAX_BUCKET_SIZE;
    int MAX_FILE_SIZE;
    int max_digits_in_hash;

    public int LD;
    Records bucket_records[];
    int next_free_space_ptr;
    int next_bucket_pointer;//points to next bucket in overflow chain
    int  elements_in_bucket;
    boolean has_next_bucket;


    Bucket(int max_size, int buck_size, int hash_digit)
    {
        LD=0;
        MAX_BUCKET_SIZE = max_size;
        MAX_FILE_SIZE = buck_size;
        max_digits_in_hash = hash_digit;

        bucket_records= new Records[MAX_BUCKET_SIZE];
        for(int i=0; i<MAX_BUCKET_SIZE; i++)
            bucket_records[i] = new Records();
        next_free_space_ptr=0;
        next_bucket_pointer=MAX_BUCKET_SIZE;
        elements_in_bucket=0;
        has_next_bucket = false;
        //fixing the inputs
        MAX_FILE_SIZE=max_size;
        MAX_BUCKET_SIZE=buck_size;
        max_digits_in_hash = hash_digit;
    }

    public String find_Binary_Value(int n, int digits)
    {
        String res="";
        int count=0;
        if(digits<0)
            digits=0;
        //int max_count_value=(int)Math.pow(2,GD_val);
        while(count<digits)
        {
            res=n%2+res;
            n=n/2;
            count++;
        }
        return res;
    }

    public void flush_bucket()
    {
        for(int i=0; i<MAX_BUCKET_SIZE; i++)
            bucket_records[i] = new Records();
        next_free_space_ptr=0;
        next_bucket_pointer=MAX_BUCKET_SIZE;
        elements_in_bucket=0;
        has_next_bucket=false;
    } //garbage collector will take care of some of the other buckets which have been created

    public int Add_Record(Bucket secondary_memory[], Records rec_insert)
    {
        if(next_free_space_ptr==MAX_BUCKET_SIZE)
        {
            if(has_next_bucket==false) // this is the last bucket, but full -> In such a case, there will be a split first -> Hence returning zero
            return 0;
            
            return secondary_memory[next_bucket_pointer].Add_Record(secondary_memory, rec_insert);
        }
        else //this is the last bucket and space remains
        {
            try{
                bucket_records[next_free_space_ptr] = rec_insert;
            }
            catch(Exception e)
            {
                System.out.println("Could not add record to bucket.");
                System.out.println("Transaction ID: "+rec_insert.trans_id);
                System.out.println("Stack Trace: ");
                e.printStackTrace();
                return 2; //code for some other non-insertion failure
            }
            elements_in_bucket++;
            next_free_space_ptr++;
            return 1; //Successful bucket insertion, no issues whatsoever
        }
    }

    public String Print_Bucket(int GD)
    {
        String res="[";
        System.out.print("[");
        for(int i=0; i<next_free_space_ptr-1; i++)
        {
            
            // res+=bucket_records[i].trans_id+"("+ find_Binary_Value(bucket_records[i].trans_id, max_digits_in_hash)+")  ";
            // System.out.print(bucket_records[i].trans_id+"("+ find_Binary_Value(bucket_records[i].trans_id, max_digits_in_hash)+")  "); //2 spaces between elements
            res+=bucket_records[i].trans_id+"("+bucket_records[i]+")  ";
            System.out.print(bucket_records[i].trans_id+"("+bucket_records[i]+")  "); //2 spaces between elements
        }
        if(next_free_space_ptr>0) // last record written separately because other wise there would be an ugly space at the end
        {
            if(bucket_records[0].trans_id!=0) //when bucket is really empty
            {
                // res+=bucket_records[next_free_space_ptr-1].trans_id+"("+ find_Binary_Value(bucket_records[next_free_space_ptr-1].trans_id, max_digits_in_hash)+")";
                // System.out.print(bucket_records[next_free_space_ptr-1].trans_id+"("+ find_Binary_Value(bucket_records[next_free_space_ptr-1].trans_id, max_digits_in_hash)+")");
                res+=bucket_records[next_free_space_ptr-1].trans_id+"("+bucket_records[next_free_space_ptr-1]+")";
                System.out.print(bucket_records[next_free_space_ptr-1].trans_id+"("+bucket_records[next_free_space_ptr-1]+")");
            }
        }
        res+="]";
        System.out.print("]");
        // else //when only one record exists in bucket
        // {
        //     if(bucket_records[0].trans_id!=0) //when bucket is really empty
        //     {
        //         res+=bucket_records[0].trans_id+"("+ find_Binary_Value(bucket_records[0].trans_id, max_digits_in_hash)+")]";
        //         System.out.print(bucket_records[0].trans_id+"("+ find_Binary_Value(bucket_records[0].trans_id, max_digits_in_hash)+")]");
        //     }
        // }
        return res;
    }


}