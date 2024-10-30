from .helper_contact import Card


def get_contacts():
    return [

        # E-MAIL
        Card(
            custom_div_text = 'E-MAIL',
            custom_h5_text = 'Possible the best choice',
            custom_a_text = '<a class="text-decoration-none link-dark stretched-link" href="mailto:dabzse.net+py__SMAP__TA__DETELE__EM__gmail.com">',
            custom_p_text = 'In general, I better like e-mail and prefer to use it',
            custom_li_items = []
        ),

        # Git
        Card(
            custom_div_text = 'Git*',
            custom_h5_text = 'Git[*] sites',
            custom_li_items = [
                '<a class="devellinks" href="http://dabzse.net/go.php?to=github" target="_blank">GitHub</a>',
                '<a class="devellinks" href="http://dabzse.net/go.php?to=gitlab" target="_blank">GitLab</a>',
            ]
        ),

        # Microsoft services
        Card(
            custom_div_text = 'Microsoft services',
            custom_h5_text = 'Microsoft services',
            custom_li_items = [
                '<a class="devellinks" href="https://teams.microsoft.com/" target="_blank">Microsoft Teams</a>',
                '<a class="devellinks" href="http://dabzse.net/go.php?to=discord" target="_blank">Discord</a>',
#                '<a class="devellinks" href="https://discord.com/users/704747410575982662" target="_blank">Discord</a>',
                '<a class="devellinks" href="skype:dr.dabzse?chat" target="_blank">Skype</a>',
                '<a class="devellinks" href="http://dabzse.net/go.php?to=linkedin" target="_blank">LinkedIn</a>',
            ]
        ),

        # Development platforms
        Card(
            custom_div_text = 'Development platforms',
            custom_h5_text = 'Development platforms',
            custom_li_items = [
                '<a class="devellinks" href="https://slack.com/" target="_blank">Slack</a>',
                '<a class="devellinks" href="https://clickup.com/" target="_blank">ClickUp</a>',
                '<a class="devellinks" href="https://asana.com" target="_blank">Asana</a>',
                '<a class="devellinks" href="https://wrike.com" target="_blank">Wrike</a>',
                '<a class="devellinks" href="https://jira.atlassian.com/" target="_blank">Jira (Atlassian)</a>',
                '<a class="devellinks" href="https://trello.com" target="_blank">Trello (Atlassian)</a>',
                '<a class="devellinks" href="https://monday.com" target="_blank">monday.com</a>',
            ]
        ),

        # JetBrains platforms
        Card(
            custom_div_text = 'JetBrains platforms',
            custom_h5_text = 'JetBrains platforms',
            custom_p_text = 'at the moment not active',
            custom_li_items = [
                '<a class="devellinks" href="https://www.jetbrains.com/youtrack/" target="_blank">YouTrack</a>',
                '<a class="devellinks" href="https://www.jetbrains.com/space/" target="_blank">Space</a>',
                '<a class="devellinks" href="https://www.jetbrains.com/datalore/" target="_blank">Datalore</a>',
                '<a class="devellinks" href="https://www.jetbrains.com/qodana/" target="_blank">Qodana</a>',
            ]
        ),

        # Flock
        Card(
            custom_div_text = 'Flock',
            custom_h5_text = 'Other',
            custom_li_items = ['<a class="devellinks" href="https://flock.com" target="_blank">Flock</a>']
        ),

        # Phone number based APPS
        Card(
            custom_div_text = 'Phone number based APPS',
            custom_h5_text = 'Phone number based apps',
            custom_p_text = 'I\'m still thinking about it, will I use these or not; so, be patient!',
            custom_li_items = ['Signal', 'Telegram', 'Viber', 'WhatsApp']
        ),

        # Matrix
        Card(
            custom_div_text = 'Matrix',
            custom_h5_text = 'Decentralized and&nbsp;safe chat',
            custom_p_text = '<img src="/static/images/qr_matrix.png" width="150" height="150" alt="QR code to Matrix chat">',
            custom_li_items = []
        ),

    ]
