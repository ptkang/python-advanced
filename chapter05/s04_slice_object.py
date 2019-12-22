import numbers
class Group():
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    # Reversible
    def __reversed__(self):
        self.staffs.reverse()

    # Sized
    def __len__(self):
        return len(self.staffs)

    # Iterable
    def __iter__(self):
        return iter(self.staffs)

    # Container
    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])

    def __str__(self):
        return str(self.staffs)


stuffs = ['Justin', 'Bob', 'Tom', 'Lily']
grp = Group('User', 'Ingneic', stuffs)
print(grp)
print(grp[1:3])
print(grp[1])
print(len(grp))

if 'Bob' in grp:
    print(True)
else:
    print(False)

for user in grp:
    print(user)

reversed(grp);
print(grp)

