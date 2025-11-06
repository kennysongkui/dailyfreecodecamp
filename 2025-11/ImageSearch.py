'''
Image Search
On November 4th, 2001, Google launched its image search, allowing people to find images using search terms. In this challenge, you will imitate the image search.

Given an array of image names and a search term, return an array of image names containing the search term.

Ignore the case when matching the search terms.
Return the images in the same order they appear in the input array.

'''


def image_search(images, term):
    matched_list = []
    for i in images:
        x = i.lower().find(term.lower())
        print(x)
        if i.lower().find(term.lower()) >= 0:
            matched_list.append(i)
    print(matched_list)
    images = matched_list[:]
    return images


t = image_search(["dog.png", "cat.jpg", "parrot.jpeg"], "dog")
print(t)

t1 = image_search(["Moon.png", "sun.jpeg", "stars.png"], "PNG")
print(t1)
