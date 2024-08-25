from django.templatetags.static import static

class AffiliateCard:
    def __init__(self, strong_text, aff_link_text, aff_link_title, aff_link_img):
        self.strong_text = strong_text
        self.aff_link_text = aff_link_text
        self.aff_link_title = aff_link_title
        self.aff_link_img = aff_link_img

    def render(self):
        aff_link_img_url = static('images/logos/' + self.aff_link_img)
        aff_link_url = f"http://dabzse.net/go.php?to={self.aff_link_text}"

        return f"""
            <div class="col">
                <div class="card mb-4 rounded-3 shadow-sm border-primary custom-card-height">
                    <div class="card-header py-3 text-bg-primary border-primary">
                        <h4 class="my-0 fw-normal text-center font-bold"><strong>{self.strong_text}</strong></h4>
                    </div>
                    <div class="card-body d-flex justify-content-center">
                        <a href="{aff_link_url}" target="_blank" title="{self.aff_link_title}">
                            <img class="affiliate" src="{aff_link_img_url}" alt="{self.strong_text}">
                        </a>
                    </div>
                </div>
            </div>
        """
