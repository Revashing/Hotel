from django.contrib import admin
from .models import PGSRoomReserving, PGSRubric, HotelEmployees, HotelRooms


class PGSRoomReservingAdmin(admin.ModelAdmin):
	list_display = ('name', 'reserving_date', 'reserving_time','price', 'cancelled')
	list_display_links = ('name', 'reserving_date', 'reserving_time', 'price')
	search_fields = ('name', 'reserving_date', 'reserving_time', 'price')


class PGSRubricAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'tags')
	list_display_links = ('name', 'description')
	search_fields = ('name', 'tags')


class HotelEmployeesAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'birth_date', 'address', 'hire_date', 'phone', 'photo')
	list_display_links = ('first_name', 'last_name', 'birth_date', 'address', 'phone', 'photo')
	search_fields = ('first_name', 'last_name', 'phone')
	readonly_fields = ('id',)


class HotelRoomsAdmin(admin.ModelAdmin):
	list_display = ('title', 'picture', 'picture_thumbnail', 'price', 'description')
	list_display_links = ('title', 'picture', 'picture_thumbnail', 'price', 'description')
	search_fields = ('title', 'price')
	readonly_fields = ('id',)


admin.site.register(PGSRoomReserving, PGSRoomReservingAdmin)
admin.site.register(PGSRubric, PGSRubricAdmin)
admin.site.register(HotelEmployees, HotelEmployeesAdmin)
admin.site.register(HotelRooms, HotelRoomsAdmin)

