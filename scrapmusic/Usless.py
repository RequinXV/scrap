









#Execution

# urls = []

# for link in getLinks(baseUrl + uri, 1674):

# # for link in getLinks(baseUrl + uri, 1):

#     print("Checking " + link)

#     urls.extend(addBaseUrl(baseUrl, swoup(link, getEndpoints)))

#     print("You'got actually :"+ str(len(urls)) + " links !")




# print(urls, "Pshatek got : " + str(len(urls)) + " links !")



# rows = []

# i = 0

# for url in urls:

#     print("Writing : " + str(i))

#     row = {}

#     row['id'] = i

#     row['category'] = ""

#     row['link'] = url

#     rows.append(row)

#     i += 1




# fieldnames = ['id', 'category', 'link']

# with open('links.csv', 'w', encoding='UTF8', newline='') as f:

#     writer = csv.DictWriter(f, fieldnames=fieldnames)

#     writer.writeheader()

#     writer.writerows(rows)

# def tryToCleanOrReturnBlank(str):

#     try:
#         result = str.getText().strip()

#     except:
#         result = ""

#     return result