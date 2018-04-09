# How gen work ?

You can easily compare gen , when we have a very slow api, we need to use gen to keep away from block
for this api ~

Test 
=========

    #terminal 1
    python lazy_response.py --port=8889

    #terminal 2
    python lazy_response.py --port=8887

    #terminal 3
    python proxy_api.py 

    #terminal 4

    curl http://localhost:8888/lz
    curl http://localhost:8888/fs
