class __schema__Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = __schema__
        exclude = ('created_at', 'updated_at')