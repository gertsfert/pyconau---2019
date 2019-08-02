
# cuDF - accelerating end-to-end data science with GPUs
* Hadoop allowed for scaling out of large data applications
* However it required writing to disk in between steps in the data science stack
* (25-100x improvement) Spark allowed for in memory processing, which did not require the disk writes
* GPU acceleration came about, however data still had to be copiied back to the CPU in between tasks (slow)
* RAPIDS allows for data to be kept in GPU memory - saving about 80% of the time for traditional GPU based computations
## Rapids and python
One of the primary focuses of RAPIDS is to be compatible with the primary Python data science librarie
## Why GPU accelerate ETL?
The average data scienctist spends 90% of their time in ETL as opossed to training models

## Challenges
* Bridge dynamiic and static languages
* Supporting operations on tables with a broad range of data types
  * Flexiible run time dispatch without code duplication
  * Miiinimising compliation complexity and time while achieving high run time performacnce
* Supporting missing/invalid data
* Enabling Python user-defined functions to operate on the GPU (just in time compilation!)
* High performane memory management

## Performance (10M rows)
* group by up to 32x speedup
* merge up to 62x
* sort up to 32x
* IO is accelerated (2GB file 25.9s -> 2s)

Key is for GPU to accelerate both loading, parsing, and decompressing.

## How to get started?
* Open source (free)
* Check out RAPIDSAI
* Conda packages in rapids AI
* Docker containers exist (docker hub, or nvidia gpu cloud registry)
* docs.rapids.ai
