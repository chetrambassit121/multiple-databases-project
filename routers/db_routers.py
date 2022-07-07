# https://docs.djangoproject.com/en/4.0/topics/db/multi-db/

class AuthRouter:
    route_app_labels = {'auth', 'contenttypes', 'sessions', 'admin'}

    def db_for_read(self, model, **hints):                                 # Suggest the database that should be used for read operations for objects of type model
        if model._meta.app_label in self.route_app_labels:
            return 'users_db'
        return None

    def db_for_write(self, model, **hints):                                 # Suggest the database that should be used for writes of objects of type Model.
        if model._meta.app_label in self.route_app_labels:
            return 'users_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None
# Return True if a relation between obj1 and obj2 should be allowed, False if the relation should be prevented, or None if the router has no opinion. 
# This is purely a validation operation, used by foreign key and many to many operations to determine if a relation should be allowed between two objects.

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'users_db'
        return None

# Determine if the migration operation is allowed to run on the database with alias db. 
# Return True if the operation should run, False if it shouldn’t run, or None if the router has no opinion.



class Blue:
    route_app_labels = {'blue'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'blue_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'blue_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'blue_db'
        return None



class Aqua:
    route_app_labels = {'aqua'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'aqua_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'aqua_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'aqua_db'
        return None