'''
URL Query Parser
Given a URL that contains a query string, parse the query string into an object (or dictionary) of key-value pairs.

The query string begins after the "?",
each parameter is separated by "&",
each key/value pair is separated by "="
For example, given "https://example.com/search?name=Alice&age=30", return:

{
  "name": "Alice",
  "age": "30"
}
All values should be returned as strings.
'''


def parse_url_query(url):
    para = url[url.index('?') + 1:]

    para_sub = para.split("&")
    print(para)
    print(para_sub)

    para_dict = {

    }

    for i in para_sub:
        key,value = i.split('=')
        print(key, value)
        para_dict[key] = value

    print(para_dict)
    url = para_dict
    return url


t = parse_url_query("https://example.com/search?name=Alice&age=30")
print(t)
