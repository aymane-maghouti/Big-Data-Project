import pandas as pd
from hdfs import InsecureClient







def store_data_in_hdfs(transaction_data):
    columns = ['id','brand','model_name','screen_size','ram','rom','cams','sim_type','battary',
               'sale_percentage','product_rating','seller_name','seller_score','seller_followers','Reviews']
    transaction_df = pd.DataFrame([transaction_data], columns=columns)

    hdfs_host = 'localhost'
    hdfs_port = 50070

    client = InsecureClient(f'http://{hdfs_host}:{hdfs_port}')


    if not client.content('/batch-layer/raw_data.csv'):
        transaction_df.to_csv('/batch-layer/raw_data.csv', index=False, header=True)
    else:
        with client.read('/batch-layer/raw_data.csv') as reader:
            existing_df = pd.read_csv(reader)
        combined_df = pd.concat([existing_df, transaction_df], ignore_index=True)
        with client.write('/batch-layer/raw_data.csv', overwrite=True) as writer:
            combined_df.to_csv(writer, index=False, header=True)







