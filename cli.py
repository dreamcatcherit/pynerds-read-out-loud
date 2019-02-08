import argparse
import sys
import utils
import click

@click.command()
@click.option("--pdf_name",prompt=True)

def test(pdf_name):
    utils.convert_pdf_to_audio(pdf_name)
    sys.stdout.write('created')


if __name__ == "__main__":
    test('')
