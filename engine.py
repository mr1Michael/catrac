class Apex_Codes:
    def __init__(self, StockCode, Description, Brand):
        self.StockCode = StockCode
        self.Description = Description
        self.Brand = Brand

    def get_category(self):
        return ApexEngine.Categorise(self.Brand, self.Description)


class ApexEngine:
    # this part is the truth. this is real. this is the part that we compare the incoming data
    # so for now cat wants it flagged/coloured when the information does not match
    BrandRules = {
        "ENERGADE": ("Sports & Energy",
                     "Cold Beverages",
                     "Beverages"),

        "LADISMITH": ("Cheese",
                      "Dairy",
                      "Chilled & Frozen Foods")
    }

    # park description rules and we can sort out local later
    DescriptionRules = {
        "GARLIC": ("Garlic",
                   "Allium",
                   "Fresh Produce")
    }

    @staticmethod
    def Categorise(brand, description):

        brand = brand.upper()
        description = description.upper()

        # Rule 1 - Brand
        if brand in ApexEngine.BrandRules:
            return ApexEngine.BrandRules[brand]

        # Rule 2 - Description
        for keyword, category in ApexEngine.DescriptionRules.items():
            if keyword in description:
                return category

        # Nothing found
        return ("Unknown",
                "Unknown",
                "Unknown")


if __name__ == "__main__":



    Energade = Apex_Codes(
        "AP19368",
        "Energade - Blueberry 24x500ml",
        "Energade"
    )

    print(Energade.get_category())
# %%
