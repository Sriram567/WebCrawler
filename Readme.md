# Readme

## Instructions to run the code:

Go to the project folder

+ Create a python environment using the below command

    ```python3 -m venv env; source env/bin/activate```

+ Install the requirements using,

    ```python -m pip install -r req.txt```
+ Give input in the input file. It has two inputs., url and depth. Write them with space.
    Example https://www.iiit.ac.in 2
+ To run the code run the following command

    ``` ./runner_script.py --path_to_HadoopStreamingJar-- --path_to_InputFile-- --input_Directory-- --path_to_MapperDirectory-- --path_to_ReducerDirectory--```

    ```./runner_script.py``` also works if you don't want to give these parameters

+ We get the graph in network.png file. And page rank graph in pagerank.png
+ Github Repo link: https://github.com/Jyotheeswar114/DS_S22_Project