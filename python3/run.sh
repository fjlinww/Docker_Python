docker run -it \
	-v $PWD/apps:/usr/src/app  \
        --device=/dev/video0 \
        --rm  wdf000/python3:20210407 face_distance.py
