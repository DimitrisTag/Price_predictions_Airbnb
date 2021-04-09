# azureai-2021-team5


Code Run : 

  Prequisities : 1) Have a folder named 'data' and inside the "listings.csv".
                 2) Have a folder named 'Project_data'.

1) Exploration    
    
    Step 1 : Run D01_Notebook.ipynb
    Step 2 : Run D02_Notebook.ipynb

2) Preprocessing 
    
    1) Mean Imputed (Missing values filled with mean, median, mode)
    Step 1 : Run amenities.py to generate the "amenities_columns.csv" in folder 'project_data'
    Step 2 : Run D03_Notebook_Mean_Imputed.ipynb to preprocess the data and generate "ListingsFinal.csv"
    
    2) KNN Imputed (Missing values filled with KNN Imputer)
    Step 1 : Run amenities.py to generate the "amenities_columns.csv" in folder 'project_data'
    Step 2 : Run D03_Notebook_KNN.ipynb to preprocess the data and generate "knn_imputed.csv"
    
3) Modeling 
    
    Step 1 : Run D04_mean_imputed.py for results of 10 fold cross-validation on "ListingsFinal.csv" 
    Step 2 : Run D04_KNN_imputed.py to results of 10 fold cross-validation on "knn_imputed.csv"
    
    
-------------------------------------------------------------------------------------------------- 
Contributors : 
1)Anastasia Mpoura
2)Kostantinos Leontaridis
3)Grigorios Tsonos
4)Anastasios Kompierovski-Stefanidis
5)Dimitrios Tagkalos



