from .helper_affiliate import AffiliateCard


def get_affiliates():
    return [

        # CHESS membership
        AffiliateCard(
            strong_text = 'see all membership plans',
            aff_link_text = 'playchess',
            aff_link_title = 'chess.com membership plans',
            aff_link_img = 'chess_premium.png',
        ),

        # CHESS profile
        AffiliateCard(
            strong_text = 'my profile on chess.com',
            aff_link_text = 'chessprofile',
            aff_link_title = 'my profile on chess.com',
            aff_link_img = 'chess_play.png',
        ),

        # GitKraken
        AffiliateCard(
            strong_text = 'GitKraken: one of the best GIT clients',
            aff_link_text = 'gitkraken',
            aff_link_title = 'GitKraken: one of the best GIT clients',
            aff_link_img = 'gitkraken.png',
        ),

        # GitLens
        AffiliateCard(
            strong_text = 'GitLens: for your IDE/TextEditor',
            aff_link_text = 'gitlens',
            aff_link_title = 'GitLens: for your IDE/TextEditor',
            aff_link_img = 'gitlens.png',
        ),

        # SideKick browser
        AffiliateCard(
            strong_text = 'SideKick web browser: chromium based, secure, privacy friendly and fast; memory efficient!',
            aff_link_text = 'sidekick',
            aff_link_title = 'SideKick web browser: chromium based, secure, privacy friendly and fast!',
            aff_link_img = 'sidekick_browser.svg',
        ),

        # WaveBox browser
        AffiliateCard(
            strong_text = 'WaveBox web browser: chromium based, secure, privacy friendly and fast!',
            aff_link_text = 'wavebox',
            aff_link_title = 'WaveBox web browser: chromium based, secure, privacy friendly and fast!',
            aff_link_img = 'wavebox_browser.svg',
        ),

        # Codeium AI code helper
        AffiliateCard(
            strong_text = 'Codeium: A free AI powered toolkit for developers | The modern coding superpower',
            aff_link_text = 'codeium',
            aff_link_title = 'Codeium: The modern coding superpower',
            aff_link_img = 'codeium.svg',
        ),

        # CodiumAI: Codiumate - AI code helper
        AffiliateCard(
            strong_text = 'Quality-first AI code generation to help busy developers write, test and review code',
            aff_link_text = 'codium',
            aff_link_title = 'Generate confidence, not just code',
            aff_link_img = 'codiumai.svg',
        ),

    ]
