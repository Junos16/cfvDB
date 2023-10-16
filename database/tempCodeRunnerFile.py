quote_page + nations_new[0])
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.find(id = 'List_of_Touken_Ranbu_Cards'))