
my_var = 'ciao'

try:
    my_var = float(my_vari)

except ValueError:
    print('Errore! non posso convertire my_var in valore numerico!')
    print('Ho avuto un errore di Valore, il valore di my_var era: "{}"'.format(my_var))

except TypeError:
    print('Errore! non posso convertire my_var in valore numerico!')
    print('Ho avuto un errore di Tipo: my_var era di tipo {}'.format(type(my_var)))

except Exception as e:
    print('Errore! non posso convertire my_var in valore numerico!')
    print('Ho avuto un errore generico: {}'.format(e))
    