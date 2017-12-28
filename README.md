## sentiment Analysis
@(demo)[jieba|sentiment|factor]
### Toolkit for the Sentiment Analysis of natural language
### The weight factor of each vocabulary dict is derived by using ???unknow

for windows
 ``` 
 ..\pyinstaller.exe --onefile --console -i <the/path/to/your/.ico> main.py 
 ```


***dir tree***
-  source dir:
    *data to analysis*
- dict dir
	*user dict*
	- degree dict 
	   - *degree adverbs*
	    ```mostdict   # 权值为2
        verydict   # 权值为1.5
        moredict # 权值为1.25
        ishdict   # 权值为0.5
        insufficientdict  # 权值为0.25
        inversedict  # 权值为-1 ```
	- emotion dict
	   - *emotional vocabulary*
    - stopwords
	   - 
    - usedict
	   - 