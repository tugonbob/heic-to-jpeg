# HEIC to JPEG Conversion Tool

A tool to bulk convert .heic files to .jpeg files in a directory and its subdirectories.

## Install Dependencies

```
pip install -r requirements.txt
```

## Usage

```
python main.py --path="/your/dir/path/here"
```

### Traverse Subdirectories

```
python main.py --path="/your/dir/path/here" -r
```

### Delete .heic Files After Conversion

```
python main.py --path="/your/dir/path/here" --replace
```
