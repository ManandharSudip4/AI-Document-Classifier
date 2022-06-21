import fitz
import pandas as pd
import os

def get_path():
    final_path = []
    path1 = input("Enter the path for AI files: ")
    print("Path Registered succesfully.")
    path2 = input("Enter the path for WEB files: ")
    print("Path Registered succesfully.")
    final_path.append(path1)
    final_path.append(path2)
    return final_path

def get_contents_from_pdf(filename):
    for path in filename:
        if '/AI' in path:
            print("--------AI Files--------")
            print(path)
            df_ai = get_Final_dataframe(path,1)
        elif '/WEB' in path:
            print("--------AI Files--------")
            print(path)
            df_web = get_Final_dataframe(path, 0)

    df =  pd.concat([df_ai,df_web])
    return df


def get_Final_dataframe(path, flags):
    contents = []
    level = []
    df = pd.DataFrame(columns=['Text', 'Label']) 
    for file in os.listdir(path):
        if file.endswith(".pdf"):
            doc = fitz.open(path+'/'+file)
            content_tmp = ''
            for page in range(len(doc)):
                content_tmp += doc[page].get_text()
                print(content_tmp)
            contents.append(content_tmp)
    df['Text'] = contents
    df['Label'] = flags
    return df

def get_content(file_path):
    # df = pd.DataFrame(columns=['Text', 'Label'])
    df = get_contents_from_pdf(file_path)

    return df


def dataset_generate():
    file_path = get_path()
    dataset = get_contents_from_pdf(file_path)
    dataset.to_csv("Dataset.csv")
        

if __name__ == "__main__":
    dataset_generate()