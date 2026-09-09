'''
Database Migration
Given two database objects, return the second object with any missing properties from the first filled in.

Fields that already exist in the record should not be overwritten.
'''

def migrate_record(schema, record):
    # print(schema)
    # for i in record.keys():
    #     print(i)
    #     if i in schema.keys():
    #         print(schema[i])
    #     else:
    #         schema[i] = record[i]
    # print(schema)

    result = dict(record)
    for key, value in schema.items():
        if key not in result:
            result[key] = value

    schema = result
    return schema

t = migrate_record({ "username": "", "posts": 0 }, { "verified": True })
print(t)