docker run -it \
	-v $PWD/apps:/usr/src/app  \
        --rm wdf000/python3 testLoadBalance.py
