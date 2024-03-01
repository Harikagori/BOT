import pandas as pd
import requests
import os
from easygui import multenterbox, msgbox


try:
    def show_error_and_exit(error_message):

       msgbox(error_message,"Error")

       exit(1)    

    # Define user input fields

    text = "Enter the following details"

    title = "Upload attachments"

    input_list = ["Jira_URL", "Username", "API_Token", "Excel_File_Path"] 

    # Get user input
    output = multenterbox(text, title, input_list)
 

    if not output:
       show_error_and_exit("you canceled the input dialog.")
 

    Jira_URL = output[0]
    Username = output[1]
    API_Token = output[2]
    Excel_File_Path = output[3]

    invalid_issues = []
    invalid_attachments = []

    upload_message =""
    invalid_message =""
    invalid_attachments_message = ""
 

    # Check if URL is valid

    if not Jira_URL.startswith("http"):

        msgbox("Invalid URL format. Please enter a valid Jira API URL starting with 'http' or 'https'.")
       

    if not Jira_URL: 
      show_error_and_exit("Please provide Jira url.")   

    if not Username: 
      show_error_and_exit("Please provide Username .")

    if not API_Token: 
      show_error_and_exit("Please provide API Token .")

    if not Excel_File_Path: 
      show_error_and_exit("Please provide Excel file path .")   


    else:
           # Read the Excel file

        df = pd.read_excel(Excel_File_Path) 

        # Check if 'Issue key' column exists in the DataFrame

        if 'Issue_key' not in df.columns:
            msgbox("The 'Issue_key' column is missing in the Excel file.")

        if   'Attachmentpath' not in df.columns:  
            msgbox("The 'Attachmentpath' column is missing in the Excel file.")

        
        else:

            # Iterate through rows and upload attachments
            successful_uploads=[]
            
            for index, row in df.iterrows():

                issue_key = row['Issue_key']

                attachment_path = row['Attachmentpath']

 

                # Check if file path is valid               

                if not os.path.exists(attachment_path):
                    
                    invalid_attachments.append(f"{issue_key}")

                    continue  # Skip this iteration

 

                # Create the attachment request

                headers = {'X-Atlassian-Token': 'no-check'}

                files = {'file': open(attachment_path, 'rb')} 

                # Define Jira API endpoint and authentication details

                jira_api_url = f"{Jira_URL}/rest/api/3/issue/{issue_key}/attachments" 

                response = requests.post(jira_api_url, auth=(Username, API_Token), headers=headers, files=files,verify=False)
                #print (response)
                
              
                if response.status_code == 200:

                    successful_uploads.append(issue_key)

                elif response.status_code == 404:
                     
                     invalid_issues.append(issue_key)               
                    
                                  
                elif response.status_code == 405:

                    msgbox("HTTP 405 Method Not Allowed: Check the Jira API URL")
            
                else:
                          msgbox(f"Failed to upload attachment for issue {issue_key}: {response.text}; {response.status_code}")

                


         # Display a summary message with both successful uploads and invalid issue keys
            if successful_uploads:

                upload_message = "Attachments uploaded successfully"

                if invalid_issues:

                    invalid_message = "Issue keys not found in Jira: " + ", ".join(invalid_issues)
                else:
                    invalid_message = "Issue keys not found in Jira: NO Invalid issues found"    

                if invalid_attachments:

                    invalid_attachments_message = "invalid attachments for issue keys: "+ ",".join(invalid_attachments)   
                else:

                    invalid_attachments_message = "invalid attachments: No invalid attachments found"                
            else:
                upload_message = "Attachments Not uploaded, Check your inputs"    


            msgbox(upload_message + "\n\n" + invalid_message + "\n\n" + invalid_attachments_message)

  

   
except requests.exceptions.RequestException as req_err:

    


    msgbox(f"Request Error: {str(req_err)}")


except Exception as e:
       
    print(f"An error occurred1: {str(e)}")