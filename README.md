# FaceTrace

Command Line tool to filter photos from a huge collection based on Face Recognition and copy the filtered photos to a separate folder.

## Setup

1. Clone the project
```console
git clone git@github.com:Sagar-D/face-trace.git
```

2. Navigate to cloned directory and create python virtual env
```console
cd face-trace
python3 -m venv .venv
```

3. Activate virtual env
```console
source .venv/bin/activate
```

4. Install dependencies
```console
pip install -r requirements.txt
```


## Execution

Note : Activate virtual env, if not already done. (Follow Step 3 under [Setup](#setup))

FaceTrace application works in 2 stages
- Stage 1 : Recursively Scan all the photos in a folder. Detect faces in each photo and tag the photos with recognized faces.
- Stage 2 : User can upload a face photo and the app will find all the photos containing uploaded face from the collection created in the previous Stage (Optionally copy the filtered photos to a new folder).


### Stage 1 + Stage 2 :

```console
python3 app.py -s <path-to-folder-containing-photos>
```

Argument "-s <path-to-folder-containing-photos>" should be passed, so that application will scan the folder for photos, detect and tag faces.

Note : The above command triggers both Stage 1 and Stage 2. This is required when scanning new photos or while executing for first time.
From next run onwards, below command can be executed to run only Stage 2


### Only Stage 2 :

```console
python3 app.py
```

