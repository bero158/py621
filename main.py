import py621
import loadereconfig
import random

# Create an unsafe api instance
api = py621.public.api(py621.types.e621)
page = random.randint(0, loadereconfig.PAGES)
perpages = 70
imageNr = random.randint(0, 70)

# Get posts from the Pool object
posts = api.getPosts(loadereconfig.TAGS,70,page,True)

post = posts[imageNr] # Select the first post from the pool

print("Post URL:")
print(post.sample.url) # Print the post's media URL