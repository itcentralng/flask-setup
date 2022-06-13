class __schema__Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = __name__
        exclude = ('created_at', 'updated_at')