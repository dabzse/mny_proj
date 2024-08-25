class Card:
    def __init__(self, custom_div_text, custom_a_text=None, custom_h5_text=None, custom_p_text=None, custom_li_items=None):
        self.custom_div_text = custom_div_text
        self.custom_a_text = custom_a_text
        self.custom_h5_text = custom_h5_text
        self.custom_p_text = custom_p_text
        self.custom_li_items = custom_li_items or []

    def render(self):
        li_elements = ''.join(f'<li>{item}</li>' for item in self.custom_li_items)

        return f"""
            <div class="col-lg-4 mb-5">
                <div class="card h-100 shadow border-0">
                    <div class="card-body p-4">
                        <div class="badge bg-primary bg-gradient rounded-pill mb-4">{self.custom_div_text}</div>
                        {f'<a class="text-decoration-none link-dark stretched-link" href="mailto:dabzse.net+py__SMAP__TA__DETELE__EM__gmail.com">{self.custom_a_text}</a>' if self.custom_a_text else ''}
                        {f'<h5 class="card-title mb-3">{self.custom_h5_text}</h5>' if self.custom_h5_text else ''}
                        {f'<p class="card-text mb-0">{self.custom_p_text}</p>' if self.custom_p_text else ''}
                        <div class="card-text mb-0">
                            <ul>
                                {li_elements}
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        """
