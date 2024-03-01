# UploadingAttachmentsIntoJIRA

#### Description
Bot can upload the Bulk Attachments into JIRA by taking attachment path and jira issue key from Excel sheet.
	
#### Author
   Gori Harika


#### Version
    1.0

#### History
|Version|Change                  |
|:------|:-----------------------|
|1.0    |Initial Baseline Version|

#### Category
	
          Technical->  string / Test operations

#### BotCategory
	 
          string / Test operations

#### Keywords
    
          API,Excel,JIRA,Attachment

#### Compatible Tool Version
    

#### Input Params
|Parameter Name         |Type       |Default Value       |Description                                                                          |
|Organization URL       |String     |NA                  |Need to provide JIRA URL of your Client or Organization                              |
|UserName               |String     |NA                  |Need to provide the username                                                         |
|Password or API_Token  |String     |NA                  |Need to provide the JIRA personal access token                                       |
|Excel file path        |String     |NA                  |Need to provide the Excel file path where attachment path and issue key are present  |
                                                         |Ex: C:\\Users\\User1\\Desktop\\JiraUploadInputfile.xlsx (Path should not be enclosed |
							 |with double quotes ("))							       |

#### Output Parameters
|Parameter Name         |Type       |Description         |    
|   |   |   |   |                       

#### Dependencies
|Dependency             |Type           |Description                                    |
|Python                 |Software       |To run the python code                         |
|Requests               |Module         |To Get,Patch the API url                       |
|pandas                 |Module         |Data manipulation and Analysis                 |
|easygui                |Module         |To Create GUIs for user input and interaction  |
|os                     |Module         |To communicate with system files/folders       |     

#### Contacts
|Contact Name           |E-Mail Id                    |Role                        |
|:----------------------|:----------------------------|:---------------------------|
|Gori Harika            |gori.harika@infosys.com      |Systems associate           |
  

#### Import Procedure
|Steps                                                                                                                          |  
|:------------------------------------------------------------------------------------------------------------------------------|
|1.Extract Jira_Issues_Attachment_Uploader.zip                                                                                  |
|2.Open Jira_Issues_Attachment_Uploader folder                                                                                  |
|3.Open dist file and you will find Jira_Issues_Attachment_Uploader.exe, to run the exe file double click                       |
|4.It will prompt for the input Jira_url,Username,PAT_Token,Excel_File_Path                                                     |
|5.After providing the values click 'OK'. New popup will open with successfull message like Attachment uploaded for all issues. |



