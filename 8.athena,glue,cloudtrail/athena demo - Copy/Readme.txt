*Normal Table* 

Upload file "annual-enterprise-survey-2017-financial-year-provisional-csv" to s3 bucket

Navigate to athena 

select create table

put the bucket location till the folder level Ex- s3://athena-nv-partitiondemo/

Insert the cloumn names and relevant data types . Skip the partition and create table .

Once query successfull prompted , perform sample queries given below 

SELECT * FROM "scoopendb"."athenademo_tbl" ;
SELECT * FROM "scoopendb"."athenademo_tbl" where Year=2017;



Partitioned table 

Create s3 bucket.
Create 3 folders inside s3 bucket named 2013,2014,2015.
Once the folders are created , upload respective data which you will find in the folders "Year=2013","Year=2014","Year=2015"
Once the data is uploaded , navigate to athena and click on create table .
While giving column values , Do not enter Year as a column. Just enter the remaining two columns.
click next and select add partition . Enter Year and INT as data type and select create table.
Once the query is successfull perform following commands to load the partitions .



ALTER TABLE scoopendb.partition_tbl_new ADD PARTITION (Year='2013') location 's3://athena-nv-partitiondemo/2013/'
ALTER TABLE scoopendb.partition_tbl_new ADD PARTITION (Year='2014') location 's3://athena-nv-partitiondemo/2014/'
ALTER TABLE scoopendb.partition_tbl_new ADD PARTITION (Year='2015') location 's3://athena-nv-partitiondemo/2015/'


Above commands will load the partitions . Once they are loaded , perform following queries to test whether performing partitions actually reduces the amount of data scanned 


[Normal Table]
SELECT * FROM "scoopendb"."athenademo_tbl";
(Run time: 0.5 seconds, Data scanned: 348.41 KB)
$1740

SELECT * FROM "scoopendb"."athenademo_tbl" where Year=2013;
 (Run time: 1.53 seconds, Data scanned: 348.41 KB)
$1740


[Partitioned Table]
SELECT * FROM "scoopendb"."partition_tbl_new"
 (Run time: 0.98 seconds, Data scanned: 174.06 KB)
$870
 SELECT * FROM "scoopendb"."partition_tbl_new" where Year=2014;
 (Run time: 2.82 seconds, Data scanned: 46.97 KB)






SELECT * FROM "scoopendb"."athenademo_tbl" ;
SELECT * FROM "scoopendb"."athenademo_tbl" where Year=2017;

CREATE EXTERNAL TABLE IF NOT EXISTS scoopendb.partition_tbl_new (
  `Industry_code_NZSIOC` bigint,
  `Value` bigint 
) PARTITIONED BY (
  Year int 
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = ',',
  'field.delim' = ','
) LOCATION 's3://athena-nv-partitiondemo/'
TBLPROPERTIES ('has_encrypted_data'='false');

Query successful. If your table has partitions, you need to load these partitions to be able to query data. You can either load all partitions or load them individually. If you use the load all partitions (MSCK REPAIR TABLE) command, partitions must be in a format understood by Hive. Learn more.