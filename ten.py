# Write a function that takes camel-cased strings (i.e.
# ThisIsCamelCased), and converts them to snake case (i.e.
# this_is_camel_cased). Modify the function by adding an argument,
# separator, so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well.



def camel_case_convert(str, arg):
    strr = "";
    print(str)
    print("==============================================================")
    for i in str:
        if i.isupper():
            strr += f"{arg}{i}"
        else:
            strr += f"{i}"
    final_str = strr[1:-1]
    print(final_str.lower())




text= "ThisIsCamelCased"
arg = "_"
camel_case_convert(text, arg)


