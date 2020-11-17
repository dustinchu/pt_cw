import csv
import requests
import timeit
from bs4 import BeautifulSoup

class Part:
    part_number = None
    quantity = None
    def __init__(self, pn, q):
        self.part_number = pn
        self.quantity = q

class PyQuoter:
    file_path = None
    url = None
    part_number_column = None
    quantity_column = None
    unit_price_column = None
    extended_price_column = None
    parts = []
    warning = []
    warning_msg = []
    csv_line = []
    sites = ['digikey'] #, 'mouser', 'rs', 'lcsc']
    pricebreak_table_index = [1] #, 0, 0, 0]
    vaild_tr_index = [2] #, 0, 0, 0]
    stock_tag_begin = ['<span id="dkQty">']#, '', '', '']
    stock_tag_end = ['</span>']#, '', '', '']
    site = None

    def get_str_between(self, line, tag1, tag2):
        start = line.find(tag1) + len(tag1)
        end = line.find(tag2, start)
        return line[start:end].replace(',', '')

    def __init__(self):
        self.file_path = input("Specify file path: ")
        #self.url = input("Specify site URL: ").lower()
        self.url = "https://www.digikey.hk/products/en?keywords="
        for s in self.sites:
            if self.url.find(s) != -1:
                self.site = self.sites.index(s)
                print("Getting quotes from " + self.sites[self.site] + ".")
                break
        part_number_column_input = input("Specify part number column: ")
        self.part_number_column = self.get_column_number(part_number_column_input)
        quantity_column_input = input("Specify quantity column: ")
        self.quantity_column = self.get_column_number(quantity_column_input)
        unit_price_column_input = input("Specify unit price column: ")
        self.unit_price_column = self.get_column_number(unit_price_column_input)
        extended_price_column_input = input("Specify extended price column: ")
        self.extended_price_column = self.get_column_number(extended_price_column_input)

    def error_handler(self, err):
        print(err)

    def show_all_parts(self):
        for p in self.parts:
            print(p.part_number)
            
    def get_column_number(self, column_string):
        column_string_char = column_string
        if column_string_char.isdigit():
            return int(column_string_char)
        elif column_string_char.isalpha():
            return (ord(column_string_char[:1].lower()) - ord('a'))
        else:
            print(quit)
            quit()

    def read_csv_file(self):
        with open(self.file_path, 'rt') as csvfile:
            rows = csv.reader(csvfile, delimiter=',', quotechar='\"')
            for row in rows:
                row_str = str(row)
                self.csv_line.append(row_str)
                part_number_str = row[self.part_number_column]
                qty_str = row[self.quantity_column].replace(',', '')
                qty = 0
                if qty_str.isdigit():
                    qty = int(qty_str)
                else:
                    return None
                part = Part(part_number_str, qty)
                self.parts.append(part)
            return rows

    def get_part_info(self, part_index):
        try:
            part_num = self.parts[part_index].part_number
            if  part_num != '':
                part_url = self.url + part_num
                req = requests.get(part_url)
                parsed = BeautifulSoup(req.content, 'html.parser')
                return parsed
        except Exception as err:
            self.error_handler(err)
            return None

    def get_part_stock(self, parsed_html):
        try:
            parsed_str = str(parsed_html)
            start = parsed_str.find(self.stock_tag_begin[self.site])
            if start == -1:
                return -1
            offset = len(self.stock_tag_begin[self.site])
            end = parsed_str.find(self.stock_tag_end[self.site], start)
            stock_str = parsed_str[start+offset:end].replace(',', '')
            stock = 0
            if stock_str != '':
                stock = int(stock_str)
            return stock
        except Exception as err:
            self.error_handler(err)

    def get_part_price(self, parsed_html, required_quantity):
        try:
            tables = parsed_html.find_all('table')
            price_break = []
            if self.site == 0:
                valid_tr = iter(tables[self.pricebreak_table_index[self.site]])
                for i in range(0, self.vaild_tr_index[self.site]):
                    next(valid_tr)
                price_break = []
                unit_price = []
                for tr in valid_tr:
                    tr_str = str(tr)
                    quantity_str = self.get_str_between(tr_str, '<td>', '</td>')
                    if quantity_str != '':
                        price_break.append(int(quantity_str))
                    price_str = (self.get_str_between(tr_str, '</td>', '</td>'))[len('\n<td>'):]
                    if price_str != '':
                        unit_price.append(float(price_str))
                up = -1.0
                pb = -1.0
                for r in range(len(price_break) - 1, -1, -1):
                    pb = price_break[r]
                    if required_quantity > price_break[r]:
                        up = unit_price[r]
                        return [pb, up]
                return [pb, up]
        except Exception as err:
            self.error_handler(err)

    def add_warning(self, warning_part_number, warning_msg):
        self.warning.append(warning_part_number)
        self.warning_msg.append(warning_msg)

    def show_warning(self):
        print("_____________________WARNING______________________")
        for i in range(0, len(self.warning)):
            print(self.warning_msg[i] + ": " + self.warning[i])

    def append_csv_file(self, target_row, up, ep):
        row_str = str(self.csv_line[target_row])
        up_in = self.insert_in_str(self.unit_price_column, row_str, up)
        ep_in = self.insert_in_str(self.extended_price_column, up_in, ep)
        self.csv_line[target_row] = ep_in

    def insert_in_str(self, target_column, string, data):
        pos = -1
        for i in range(0, target_column):
            pos = string.find(',', pos + 1)
            if pos == -1:
                i = i - 1
                string = string + ','
        return string[:pos] + ',\'' + str(data) +'\'' + string[pos:]

    def rewrite_csv_file(self):
        with open(self.file_path[:len(self.file_path) - 4] + '_quoted.csv', 'a+') as csvfile:
            for i in range(0, len(self.csv_line)):
                replace_str = self.csv_line[i].replace('[', '').replace(']', '').replace('\'', '')
                csvfile.write(replace_str)
                csvfile.write('\n')
            csvfile.close()

    def get_quote(self, supress_console_output):
        start_time = timeit.default_timer()
        self.read_csv_file()
        for i in range(0, len(self.parts)):
            try:
                if not supress_console_output:
                    print("__________________________________________________")            
                part_number = self.parts[i].part_number
                quantity = self.parts[i].quantity
                if not supress_console_output:
                    print("PART: " + str(part_number))
                    print("QUANTITY: " + str(quantity))
                html = self.get_part_info(i)
                stock = self.get_part_stock(html)
                if stock == -1:
                    self.add_warning(part_number, "MULTIPLE FOUND")
                    if not supress_console_output:
                        print("MULTIPLE FOUND FOR: " + part_number)
                    continue
                if(stock < quantity):
                    self.add_warning(part_number, "LOW STOCK")
                    if not supress_console_output:
                        print("LOW STOCK: " + str(stock))
                    continue
                prices = self.get_part_price(html, quantity)
                unit_price = prices[1]
                price_break = prices[0]
                if unit_price == -1.0:
                    self.add_warning(part_number, "MOQ NOT REACHED")
                    if not supress_console_output:
                        print("MOQ NOT REACHED:" + str(prices[0]))
                    continue
                else:
                    extended_price = round(unit_price * quantity, 2)
                    try:
                        self.append_csv_file(i, unit_price, extended_price)
                    except:
                        pass
                    if not supress_console_output:
                        print("PRICE BREAK: " + str(price_break))
                        print("UNIT PRICE: " + '{0:.5f}'.format(unit_price))
                        print("EXTENDED PRICE: " + '{0:.2f}'.format(extended_price))
            except Exception as err:
                self.add_warning(part_number, str(err))
                if not supress_console_output:
                    print(err)
                    continue
        try:
            self.rewrite_csv_file()
        except:
            pass
        end_time = timeit.default_timer()
        delta_time = end_time - start_time
        if not supress_console_output:
            if len(self.warning) != 0:
                self.show_warning()
            print("__________________END OF QUOTE____________________")
        print("QUOTATION COMPLETED IN " + '{0:.3f}'.format(delta_time) + " SECONDS.")

def main():
    py = PyQuoter()
    py.get_quote(False)

if __name__ == "__main__":
    main()