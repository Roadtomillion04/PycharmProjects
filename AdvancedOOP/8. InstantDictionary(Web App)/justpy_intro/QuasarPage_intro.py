# Quasar is interface from vue.js
# Refer Quasar for documentation
import justpy as jp

wp = jp.QuasarPage() # provides advanced components

# But for styling in Quasar we can't customize it's very basic
# So for styling set tailwind=True,
web = jp.QuasarPage(tailwind=True)

# The tags for Quasar also different
jp.QDiv()
jp.QBtn()
