import bs4 as bs
import requests


def scrape_player_data():
    """ Goes to data site, pulls salary info and returns in descending order """

    # scrape data from website
    resp = requests.get(
        'https://questionnaire-148920.appspot.com/swe/data.html')  # Access website
    soup = bs.BeautifulSoup(resp.text, 'html.parser')
    table = soup.find('table', {'id': 'salaries-table'})  # Find salaries-table

    player_salary = []
    for row in table.findAll('tr'):
        # For each row in table, find and copy player salary
        salary = row.find('td', {'class': 'player-salary'}).text.strip()

        # Clean up data, removing all non integers and empty strings
        if salary == 'no salary data' or salary == '':
            salary = '0'
        salary = salary.replace("$", '')
        salary = salary.replace(",", '')

        # Append to array as an integer
        player_salary.append(int(salary))

    # Sort the array in descending order
    player_salary.sort(reverse=True)

    return player_salary


def qualifying_offer(salary):
    """Calculate qualifying offer"""
    return (sum(salary[:125]) / 125)


def display_results():
    """ Display relevant information to user """

    # Scape the data from website
    player_salary = scrape_player_data()

    print(f"\nHighest Salary: ${player_salary[0]:,.2f}")
    print(f"Lowest Salary: ${player_salary[125]:,.2f}")
    print(f"Qualifying offer: ${qualifying_offer(player_salary):,.2f}\n")
    


if __name__ == "__main__":
    display_results()
