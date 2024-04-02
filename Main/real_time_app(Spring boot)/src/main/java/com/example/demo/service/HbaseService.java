package com.example.demo.service;

import java.util.Map;

import org.springframework.stereotype.Service;
import org.apache.hadoop.hbase.Cell;
import org.apache.hadoop.hbase.CellUtil;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.TableName;
import org.apache.hadoop.hbase.client.*;
import org.apache.hadoop.hbase.util.Bytes;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;




@Service
public class HbaseService {

	
	  public static Map<String, String> decodeMap(Result result) {
	        Map<String, String> decodedMap = new HashMap<>();
	        for (Cell cell : result.rawCells()) {
	            String family = Bytes.toString(CellUtil.cloneFamily(cell));
	            String qualifier = Bytes.toString(CellUtil.cloneQualifier(cell));
	            String value = Bytes.toString(CellUtil.cloneValue(cell));
	            String key = family + ":" + qualifier;
	            decodedMap.put(key, value);
	        }
	        return decodedMap;
	    }

	    public static Map<String, String> getLastRecordFromHBase() throws IOException {
	        org.apache.hadoop.conf.Configuration config = HBaseConfiguration.create();
	        config.set("hbase.zookeeper.quorum", "localhost"); // Assuming HBase is running locally

	        Connection connection = ConnectionFactory.createConnection(config);
	        Table table = connection.getTable(TableName.valueOf("smartphone"));

	        Scan scan = new Scan();
	        scan.setReversed(true);
	        scan.setMaxResultSize(1);

	        ResultScanner scanner = table.getScanner(scan);
	        Result result = scanner.next();

	        Map<String, String> lastRecord = new HashMap<>();
	        if (result != null) {
	            lastRecord = decodeMap(result);
	        }

	        scanner.close();
	        table.close();
	        connection.close();

	        return lastRecord;
	    }
	
	
}
