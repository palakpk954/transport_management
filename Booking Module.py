class Booking(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    booking_date = models.DateField(auto_now_add=True)
