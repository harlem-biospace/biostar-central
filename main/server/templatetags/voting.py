from django import template
from main.server import const

register = template.Library()

def votebox(context, post, up, down):
    return { 'post':post, 
             'upvoted': post.id in up,
             'downvoted': post.id in down,
            #'upvoted': post.get_vote(context['user'], const.VOTE_UP) is not None,
            #'downvoted':post.get_vote(context['user'], const.VOTE_DOWN) is not None
			}



register.inclusion_tag('widgets/votebox.html', takes_context=True)(votebox)





